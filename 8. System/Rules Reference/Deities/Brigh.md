---
type: deity
source-type: "Remaster"
domains: "Creation, Knowledge, Metal, Time"
favored-weapon: "Light-hammer"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Temporary Tool]], Rank 4: [[Creation]], Rank 7: [[Duplicate Foe]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Brigh's exact origins are unknown, though her priests and various religious scholars have many theories on the matter. Some believe she was a construct who achieved consciousness and a spark of divinity, while others think she was a human alchemist and inventor who discovered ways to fuse mechanical components with her own physiology. Regardless of her origins, Brigh is a patient and thoughtful god who promotes unending curiosity and constant intellectual advancement. Her two most common forms are a humanoid woman made of bronze clockwork and a human woman wearing a bronze skullcap and armor composed of gears and other movable metal pieces. Though Brigh's usual demeanor is composed and reserved, she isn't an unfeeling automaton; she deeply cherishes the creations she and her followers make, and most of her worshippers feel the same way.

**Title** The Whisper in Bronze

**Areas of Concern** clockwork, invention, time

**Edicts** craft new creations, pay attention to details, share achievements

**Anathema** carelessly destroy others' creations or research, enslave intelligent constructs, abuse constructs, refuse to acknowledge or learn from mistakes

**Religious Symbol** mask with forehead runes

**Sacred Animal** termite

**Sacred Color** bronze, silver

**Source:** `= this.source` (`= this.source-type`)
