---
type: deity
source-type: "Remaster"
domains: "Death, Duty, Fate, Glyph"
favored-weapon: "Warhammer"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Temporary Tool]], Rank 2: [[Expeditious Excavation]], Rank 8: [[Earthquake]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Magrim is not the leader of the dwarven pantheon, but he holds a special place of honor and authority as the eldest among them. As the dwarven deity of both fate and death, his solemn duty is to ensure that every dwarf born on Golarion is granted both a unique mortal purpose and an achievable path to its fulfillment; the specifics of this charge vary from dwarf to dwarf, frequently focusing on the creation of something great and wonderful that will long outlast its creator. The faith of Magrim teaches that few tasks are of more paramount importance than ensuring that time-honored traditions are properly observed, that dwarven language and culture remain as constant and unchanging as possible, and that all dwarves are provided with access to whatever knowledge and tools are necessary to accomplish that which is expected of them. The surest path to a productive and satisfying mortal existence is to carefully follow one's prescribed destiny and purpose, and while those who choose to eschew this purpose in favor of forging their own paths are not shunned or looked down upon, conventional sentiment is that a dwarf who ignores the instructions clearly laid out for them by the Taskmaster does so at their own peril.

In addition to providing parishioners with guidance to live a proper life, priests of Magrim are responsible for laying the dead to rest in accordance with dwarven tradition, as well as swiftly and mercilessly dealing with grave robbers, necromancers, and others who would disturb the deceased. As befits a deity favored by artisans and workers, Magrimite centers of worship frequently double as places of work: most commonly mines and forges, but also shops, taverns, and more esoteric establishments such as bakeries and scriveners. A temple or shrine to Magrim is traditionally decorated with ornate runic inscriptions relaying key tenets of the Taskmaster's doctrines, for Magrim is also the patron of runes, and the masons who employ them etch his teachings into timeless stone to guide future generations.

**Title** The Taskmaster

**Areas of Concern** Death, fate, underworld

**Edicts** Perfect a craft or trade, carve runes, destroy undead, aid others with completing unfinished tasks

**Anathema** Treat grave sites irreverently, mistreat your tools, create undead, damage a soul

**Religious Symbol** rune-carved cave entrance

**Sacred Animal** mole

**Sacred Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
