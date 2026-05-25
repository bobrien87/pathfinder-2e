---
type: deity
source-type: "Remaster"
domains: "Creation, Earth, Family, Protection"
favored-weapon: "Warhammer"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Mindlink]], Rank 3: [[Earthbind]], Rank 4: [[Creation]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

"Subtle as a hammer" is a phrase commonly uttered about both worshippers of Torag and the god himself. Torag, while not the only dwarven deity, is arguably the most well-known among the other peoples of Golarion. His is the most general of worship within the dwarven pantheon, less focused on specific aspects of worship and more the bedrock upon which the others depend. He is often depicted as an older dwarf man, obviously rugged and mighty in his scarred, runic armor. His hammer, Kaglemros, is etched with his imposing visage, eyes blazing with the inner fire hotter than any forge. He counts crafters among his most ardent followers, be they workers of metal, stone, or cloth. Not to be outshone, soldiers and mercenaries often pray to Torag in his aspect as protector, praying that no harm will come to them or their companions as they take the fight to those who wish harm upon what they defend. In his secondary aspect as a defensive strategist, he grants battle wisdom to his followers, allowing them to see strategies and exploit opponents' vulnerabilities on the field of combat.

**Title** Father of Creation

**Areas of Concern** forge, protection, strategy

**Edicts** be honorable and forthright, keep your word, respect the forge, serve your people

**Anathema** tell lies or cheat someone, intentionally create inferior works, show continued mercy to the enemies of your people when such enemies prove they are undeserving

**Religious Symbol** iron hammer

**Sacred Animal** badger

**Sacred Colors** gold, gray

**Source:** `= this.source` (`= this.source-type`)
