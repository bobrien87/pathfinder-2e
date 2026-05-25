---
type: deity
source-type: "Remaster"
domains: "Darkness, Glyph, Knowledge, Secrecy"
favored-weapon: "Lance"
divine-font: "Harm"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Befuddle]], Rank 4: [[False Nature]], Rank 7: [[Warp Mind]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Nyuo-ogh appears as a floating lizard eye surrounded by a darkness from which small grasping claws appear to grab at anything in their reach. The Always Observing was recently born from one of Oaur-Ooung's blisterwombs, making him the youngest qlippoth lord in existence. Nyuo-Ogh seeks to plunge mortalkind into literal and educational darkness, eradicating both science and magic. He believes this will radically shorten mortal life spans and capacity for sin, with the additional effect of erasing their understanding of the rituals used to contact demons. As part of this process, Nyuo-Ogh constantly watches the mortal planes, looking for ways to slow the advancement of knowledge.

**Title** The Always Observing

**Areas of Concern** Destruction of knowledge, eternal darkness, unraveling of magic

**Edicts** Kill other practitioners of magic, obliterate systems of education, watch your enemies and learn from them

**Anathema** Educate others, rely too much on magic

**Religious Symbol** shadowy rune shaped like a lizard eye

**Sacred Animal** none

**Sacred Colors** purple

**Source:** `= this.source` (`= this.source-type`)
