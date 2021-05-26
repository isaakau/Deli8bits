# Deli8bits
*Postres es la aplicación y deli8Bits es el proyecto


create user PRODD8B IDENTIFIED by deli;
grant connect, resource to  PRODD8B;
alter user PRODD8B default tablespace users quota unlimited on users;