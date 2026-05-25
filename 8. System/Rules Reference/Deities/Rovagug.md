---
type: deity
source-type: "Remaster"
domains: "Air, Destruction, Earth, Zeal"
favored-weapon: "Greataxe"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 2: [[Enlarge]], Rank 6: [[Disintegrate]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Known by titles such as the Rough Beast, the Imprisoned King, the Tide of Fangs, the Unmaker, and the Worldbreaker, Rovagug is the god of destruction, disaster, and wrath. The Rough Beast is not a benevolent or kind deity. Among the other gods, Rovagug has no allies and almost every mortal fears and despises him; not that he would care. Rovagug's only desire is to consume all that lives and crush the rest. It's what he was born to do, is all he cares about, and nothing can sway him from his goal. Left unchecked, he might have destroyed all of creation millennia ago. Most mortals would therefore consider it lucky that the qlippoth lord has been imprisoned since the Age of Creation.

**Title** The Rough Beast

**Areas of Concern** destruction, disaster, wrath

**Edicts** destroy all things, free Rovagug from his prison

**Anathema** create something new, let material ties restrain you, torture a victim or otherwise delay its destruction

**Religious Symbol** fanged spider

**Sacred Animal** scorpion

**Sacred Colors** brown, red

**Source:** `= this.source` (`= this.source-type`)
