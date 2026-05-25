---
type: deity
source-type: "Remaster"
domains: "Change, Magic, Protection, Time"
favored-weapon: "Dagger"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 2: [[Knock]], Rank 4: [[Translocate]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Alseta holds sway over transitions. Physical transitions through doorways and portals or over thresholds, metaphorical transitions, and even the forward flow of time-Alseta influences them all. She watches over city gates, helping keep invaders out and defenders safe. She also watches over those moving into a new stage in life, whether that means a birthday, a marriage, or a more fitting body. It is common for anyone entering into a life change, such as moving to a new town or changing careers, to look to Alseta for guidance. Likewise, birth and death are both transitions, and expectant mothers and the bereaved both offer her prayers, linking Alseta's church to that of [[Pharasma]]. Some consider Alseta to be the goddess of teleportation, though she does not officially claim that title. She is also a popular god among some elven nations and cultures, who frequently associate Alseta with the *aiudara*, or elf gates, around Golarion.

**Title** The Welcomer

**Areas of Concern** doors, portals, thresholds, traditions

**Edicts** offer to protect passageways and guide others through transitions, treat all other beings with courtesy and respect

**Anathema** destroy a door or block a path for personal gain, stop transition without good reason

**Religious Symbol** two faces in profile

**Sacred Animal** tortoise

**Sacred Color** brown, gray

**Source:** `= this.source` (`= this.source-type`)
