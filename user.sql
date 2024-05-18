-- cursor.execute("INSERT INTO users (name, surname, token) VALUES ('admin', 'admin', '0004650166692')")
create table `users` (
    `id` integer primary key autoincrement,
    `name` text not null,
    `surname` text not null,
    `token` text not null
);
insert into `users` (name, surname, token) values ('admin', 'admin', '0004650166692');
insert into `users` (name, surname, token) values ('user', 'user', '0004650166693');
insert into `users` (name, surname, token) values ('user2', 'user2', '0004653466693');
insert into `users` (name, surname, token) values ('user3', 'user3', '0004650166694');
insert into `users` (name, surname, token) values ('user4', 'user4', '0004650166695');