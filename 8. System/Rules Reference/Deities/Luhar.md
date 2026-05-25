---
type: deity
source-type: "Remaster"
domains: "Cities, Darkness, Dreams, Sun"
favored-weapon: "Spiked-chain"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Sleep]], Rank 3: [[Shared Invisibility]], Rank 5: [[Umbral Journey]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The old gods of the threefold sun were all but forgotten under the rule of [[Walkena]]-but Luhar did not mind being forgotten. It is Walkena's undeath that she finds offensive, for she had crafted him such a beautifully perfect eternal sleep. Now he not only rejects her gift, but instills so much fear in his followers that their rest is fitful and brief.

**Title** The Setting Sun

**Areas of Concern** Death, dreams, destiny

**Edicts** Learn about the night and prepare yourself to face its creatures and dangers, always make time for sleeping and dreams, ensure others never go to sleep scared

**Anathema** Stay up all night without any breaks for sleeping or dreaming, attack a person or creature while they sleep, leave a badly wounded opponent alive and suffering, create undead or ask questions of the dead

**Religious Symbol** silver face in the setting sun

**Sacred Animal** lion

**Sacred Colors** black, silver

**Source:** `= this.source` (`= this.source-type`)
