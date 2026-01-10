# scripts/create_superuser.py
import asyncio
import sys

from sqlalchemy import select

from app.core.security import get_password_hash
from app.db.models import User

# Ajusta estos imports según tu estructura de carpetas real
from app.db.session import get_db
from app.schemas.enums import UserRole


async def create_superuser(email: str, password: str):
    async for session in get_db():
        # 1. Verificar si ya existe
        result = await session.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()

        if user:
            print(f"⚠️  El usuario {email} ya existe.")
            return

        # 2. Crear el usuario manualmente (bypass de validaciones de API para forzar rol)
        print(f"🔨 Creando superusuario {email}...")
        new_user = User(
            email=email,
            hashed_password=get_password_hash(password),
            full_name="Super Admin",
            role=UserRole.ADMIN,  # <--- Aquí forzamos el rol
        )

        session.add(new_user)
        await session.commit()
        print(f"✅ Superusuario {email} creado exitosamente.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: uv run scripts/create_superuser.py <email> <password>")
        sys.exit(1)

    email_arg = sys.argv[1]
    pass_arg = sys.argv[2]

    asyncio.run(create_superuser(email_arg, pass_arg))
