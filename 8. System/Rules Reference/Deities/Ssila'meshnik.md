---
type: deity
source-type: "Remaster"
domains: "Fate, Freedom, Knowledge, Trickery"
favored-weapon: "Light-hammer"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Liberating Command]], Rank 4: [[Mirror'S Misfortune]], Rank 5: [[Synaptic Pulse]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ssila'meshnik holds answers and freedom for all who call on them. They are the protean lord of fate, freedom, and paradox, and though they see the paths of all possible futures, the present is often out of reach. They exist as a flurry of shadowed afterimages, cast out across the infinite branches of time and choice. Though the Colorless Lord knows the twists and turns all lives take, those who call on them inevitably turn away from the answers the lord provides. Those who call on Ssila'meshnik always abandon their path.

**Title** The Colorless Lord

**Areas of Concern** Fate, freedom, paradox

**Edicts** Embrace change, pursue freedom, present opposing perspectives, seek out new skills and experiences

**Anathema** Adhere to a single fate, honor an oath you are not expected to break, sow compromise among opposing groups

**Religious Symbol** triquetra over a keketar head

**Sacred Animal** barnacle goose

**Sacred Colors** none

**Source:** `= this.source` (`= this.source-type`)
