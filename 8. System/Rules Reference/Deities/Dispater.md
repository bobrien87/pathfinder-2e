---
type: deity
source-type: "Remaster"
domains: "Cities, Confidence, Duty, Tyranny"
favored-weapon: "Mace"
divine-font: "Harm"
divine-skill: "Society"
divine-spells: "Rank 1: [[Tether]], Rank 4: [[Suggestion]], Rank 6: [[Petrify]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Hell's second layer is the Diabolic City, Dis, and its ruler is the archdevil Dispater. The Iron Lord is the architect of the orderly perfection of Hell as a blueprint for the rest of the multiverse, responsible for Dis's own vile and startling perfection. He remains distant from the scheming and machinations of the other archdevils and the Universe, instead modeling calm and deliberate action combined with ruthless, merciless arrogance. As the most urbane of the archdevils, he attracts many followers among those who wish to see Hell's dark majesty spread across the universe.

**Title** Iron Lord

**Areas of Concern** Cities, prisons, rulership

**Edicts** Uphold absolute law, pursue perfection in your surroundings, speak with refinement

**Anathema** Act above your station, neglect your defenses, betray a lover

**Religious Symbol** iron nail, crown, and ring

**Sacred Animal** hound

**Sacred Colors** iron gray, red

**Source:** `= this.source` (`= this.source-type`)
