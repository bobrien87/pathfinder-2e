---
type: deity
source-type: "Remaster"
domains: "Change, Fate, Nature, Water"
favored-weapon: "Spear"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 3: [[Aqueous Orb]], Rank 5: [[Control Water]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Lysianassa, Empress of the Torrent, is the elemental lord of currents, tides, and water. The benevolent lord of water patrols her plane as a powerful sailfish made of coral and streaked with mother of pearl, creating the ocean's currents in her wake. Lysianassa tends to the tides and their victims, cultivating change and nurturing the growth that water so often provides. Fearful of stagnancy after a long imprisonment, she races the waves of her own creation and encourages others to do the same.

**Title** Empress of the Torrent

**Areas of Concern** Currents, flow, oceans, tides, water

**Edicts** Change to avoid stagnation, promote life and growth, respect and aid the flow of natural cycles, swim

**Anathema** Dam a river, disrespect sincere gifts of water or drink, pollute clean bodies of water

**Religious Symbol** two waves feeding each other

**Sacred Animal** nautilus

**Sacred Colors** coral, blue

**Source:** `= this.source` (`= this.source-type`)
