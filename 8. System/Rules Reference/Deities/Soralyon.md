---
type: deity
source-type: "Remaster"
domains: "Creation, Earth, Magic, Protection"
favored-weapon: "Pick"
divine-font: "Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Summon Construct]], Rank 3: [[One With Stone]], Rank 4: [[Mountain Resilience]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Guardians, monuments, and magic are the purview of the Mystic Angel. Soralyon believes that monuments and ruins are important links to the past. Guarding them against those who would defile or destroy them is of tremendous importance, lest people lose memories of who they are, where they came from, and what they have accomplished. As such, those who stand guard over monuments and ruins are blessed. Likewise, those who study monuments to the past and present with respect, or seek to preserve them for the future, are also blessed. Guardianship of others, but especially of those who study and preserve these relics to the past, is also of great importance to Soralyon. As magic is a valuable tool in guarding, studying, and preserving these monuments and people, Soralyon encourages the study of magic, preferably for use in learning or protection.

**Title** The Mystic Angel

**Areas of Concern** Guardians, magic, monuments

**Edicts** Study monuments, craft golems and artwork from stone, guard ancient sites

**Anathema** Defile sacred buildings, knowingly unearth evil monuments, destroy historical artifacts

**Religious Symbol** rune-covered spire

**Sacred Animal** guard dog

**Sacred Colors** gray, purple

**Source:** `= this.source` (`= this.source-type`)
