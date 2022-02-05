select * from post;

CREATE SEQUENCE comment_id_seq;
alter table comment
 alter column id set default nextval('comment_id_seq');
ALTER TABLE comment ALTER COLUMN id SET NOT NULL;
ALTER SEQUENCE comment_id_seq OWNED BY comment.id;

delete from post where id=4;