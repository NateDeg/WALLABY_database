\connect wallabydb

-- Ownership to admin
ALTER TABLE wallaby.run OWNER TO "admin";
ALTER TABLE wallaby.instance OWNER TO "admin";
ALTER TABLE wallaby.detection OWNER TO "admin";
ALTER TABLE wallaby.product OWNER TO "admin";
ALTER TABLE wallaby.source OWNER TO "admin";
ALTER TABLE wallaby.source_detection OWNER TO "admin";
ALTER TABLE wallaby.tag OWNER TO "admin";
ALTER TABLE wallaby.comment OWNER TO "admin";
ALTER TABLE wallaby.tag_source_detection OWNER TO "admin";
ALTER TABLE wallaby.external_conflict OWNER TO "admin";
ALTER TABLE wallaby.kinematic_model OWNER TO "admin";
ALTER TABLE wallaby.wkapp_product OWNER TO "admin";

-- Admin privileges
GRANT ALL PRIVILEGES ON DATABASE wallabydb TO "admin";
GRANT ALL PRIVILEGES ON DATABASE wallabydb TO "gavoadmin";
GRANT ALL PRIVILEGES ON DATABASE wallabydb TO "gavo";

-- Read-only wallaby user
GRANT CONNECT ON DATABASE wallabydb TO "wallaby_user";
GRANT USAGE ON SCHEMA "wallaby" TO "wallaby_user";
GRANT SELECT ON ALL TABLES IN SCHEMA "wallaby" to "wallaby_user";
GRANT SELECT ON ALL SEQUENCES IN SCHEMA wallaby TO "wallaby_user";

-- Read-only cirada
GRANT CONNECT ON DATABASE wallabydb TO "cirada";
GRANT USAGE ON SCHEMA "wallaby" TO "cirada";
GRANT SELECT ON ALL TABLES IN SCHEMA "wallaby" to "cirada";
GRANT SELECT ON ALL SEQUENCES IN SCHEMA wallaby TO "cirada";
GRANT ALL PRIVILEGES ON TABLE wallaby.kinematic_model, wallaby.wkapp_product, wallaby.wrkp_product TO "cirada";

-- Read only SPSRC user

-- Permissions for VO services
GRANT CONNECT ON DATABASE wallabydb TO "gavoadmin";
GRANT USAGE ON SCHEMA "wallaby" TO "gavoadmin";
GRANT SELECT ON ALL TABLES IN SCHEMA "wallaby" TO "gavoadmin";
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA wallaby TO "gavoadmin";

GRANT CONNECT ON DATABASE wallabydb TO "gavo";
GRANT USAGE ON SCHEMA "wallaby" TO "gavo";
GRANT SELECT ON ALL TABLES IN SCHEMA "wallaby" TO "gavo";
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA wallaby TO "gavo";

-- Other
GRANT CONNECT ON DATABASE wallabydb TO "untrusted";
GRANT USAGE ON SCHEMA "wallaby" TO "untrusted";
GRANT SELECT ON TABLE wallaby.run, wallaby.instance, wallaby.detection, ALTER TABLE wallaby.kinematic_model OWNER TO "admin"; wallaby.product, wallaby.source, wallaby.source_detection, wallaby.tag, wallaby.tag_source_detection, wallaby.comment, wallaby.external_conflict, wallaby.kinematic_model, wallaby.wkapp_product TO "untrusted";
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA wallaby TO "untrusted";
