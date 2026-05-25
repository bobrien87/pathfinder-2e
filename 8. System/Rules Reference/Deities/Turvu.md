---
type: deity
source-type: "Remaster"
domains: "Freedom, Introspection, Knowledge, Travel"
favored-weapon: "Claw, Staff"
divine-font: "Harm, Heal"
divine-skill: "Religion"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 4: [[Translocate]], Rank 5: [[Cloak Of Colors]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

As Apsu and Sarshallatu imagined their offspring, they deigned that one needed to understand the responsibility that comes with divinity. Thus, Turvu was born. Yet as Turvu witnessed the turmoil and violence erupting within their own family, they fled the chaos boiling around them.

Turvu found themself drawn to exploration rather than a stagnant lifestyle. They devoted their time to understanding each plane of existence and the variety of magic, resources, and beauty that could be found there. Through their travels, Turvu began to understand the very essence of divinity and found little use for the division of the good and the evil.

A being that exists beyond the binary of beliefs, Turvu's very consciousness spans multiple planes of existence, defying the conventional laws of space and time. Lithe and more serpentine than other dragons, with kaleidoscopic scales that seem to shift to match their surroundings, Turvu's features and general demeanor allow them to integrate on any plane, be it in Heaven, Hell, or beyond.

**Title** The Shifting Plane

**Areas of Concern** death of ego, divinity, philosophy

**Edicts** travel and explore the world and other planes, seek to understand all sides of a conflict

**Anathema** deem anything purely good or evil without first seeking context, remain stagnant in the pursuit of exploration or knowledge

**Religious Symbol** a prism with many sides reflecting many colors

**Sacred Animal** none

**Sacred Colors** white

**Source:** `= this.source` (`= this.source-type`)
