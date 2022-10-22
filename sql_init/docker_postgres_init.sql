create table users
(
    id        serial
        primary key,
    user_name varchar,
    state     varchar,
    position  varchar
);

alter table users
    owner to postgres;


