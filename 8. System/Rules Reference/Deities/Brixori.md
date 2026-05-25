---
type: deity
source-type: "Remaster"
domains: "Glyph, Introspection, Knowledge, Magic"
favored-weapon: "Starknife"
divine-font: "Harm, Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Déjà Vu]], Rank 3: [[Threefold Aspect]], Rank 5: [[Summon Dragon]], Rank 8: [[Quandary]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Born the smallest and weakest of her clutch, Brixori was often teased and bullied by her other siblings, none more so than her violent brother Dahak. Dahak left Brixori alive when he tore his other siblings asunder, either out of piteous contempt or because he simply forgot she existed—Brixori has never been clear on which.

As a young dragon, Brixori sought solace in uncovering esoteric knowledge from the hidden recesses of the multiverse. Through years of rigorous study and unwavering determination, Brixori's command over occult magic grew formidable. She mastered the art of communing with spirits, bending shadows to her will, and invoking ancient rites that could alter the fabric of reality itself.

Though her power is great, Brixori prefers to remain in the shadows of her other siblings. She considers the libraries of Golarion her true hoard and often uses a humanoid avatar to spend her days among the university stacks. Brixori feels more comfortable conversing with mortals in this form, preferring quiet locations and conversations held in hushed voices. For those wise enough to see through her disguise, she is a gentle and generous deity. For those foolish enough to cross her, her wrath is swift and severe.

Brixori's influence extends beyond her fellow dragons, touching the lives of mortals who seek her guidance in the occult arts. She is beacon for those who yearn for knowledge and power beyond the mundane, a patron of the mystical and the supernatural. Her followers, a diverse assembly of witches, oracles, and scholars, revere her not only for her power, but for her journey from underestimated runt to a goddess of unparalleled occult mastery.

**Title** The Wayward Sister

**Areas of Concern** libraries, the supernatural, underdogs

**Edicts** pursue knowledge even in the most unusual places, seek to understand that which cannot be explained, show kindness to those who are weaker than the rest

**Anathema** underestimate an enemy or an ally, treat those weaker than you unkindly

**Religious Symbol** a deep purple, gem-encrusted tome

**Sacred Animal** dragonfly

**Sacred Colors** purple, black, silver

**Source:** `= this.source` (`= this.source-type`)
