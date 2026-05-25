---
type: deity
source-type: "Remaster"
domains: "Death, Fate, Healing, Knowledge"
favored-weapon: "Dagger"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Mindlink]], Rank 3: [[Ghostly Weapon]], Rank 4: [[Vision Of Death]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Before there was time, or even a sun or moon by which to measure it, there was a beginning. That beginning had an end, which led to another fresh start. This spiral of time winds out forever, glimmering in the space between spaces. At the center of that spiral sits the Spire, and atop that Spire sits Pharasma, the Lady of Graves, goddess of death, birth, fate, and prophecy. The Lady of Graves is often depicted in a triptych of her three forms—an older midwife with silver hair pulled back into a harsh braid to keep it out of her face, a young prophet with wild hair that frames her face, and a tall, regal woman in black robes atop a throne of skulls, holding an hourglass full of blood red sand. Across all forms, Pharasma's silver hair, ashen skin, and white eyes are a constant.

**Title** The Lady of Graves

**Areas of Concern** birth, death, fate, prophecy, time

**Edicts** strive to understand ancient prophecies, destroy undead, lay bodies to rest

**Anathema** create undead, desecrate a corpse, take from the dead in bad faith

**Religious Symbol** spiraling comet

**Sacred Animal** whippoorwill

**Sacred Colors** blue, white

**Source:** `= this.source` (`= this.source-type`)
