---
type: deity
source-type: "Remaster"
domains: "Death, Decay, Plague, Undeath"
favored-weapon: "Spiked-chain"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 3: [[Envenom Companion]], Rank 5: [[Toxic Cloud]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Preceded by the stench of sun-ripened corpses, one is never caught unawares by Nergal. The sights of the battlefield, driving many mortals to teary eyes and corkscrewed mouths holding back retches, stir him with giddy laughter from his many orifices. Classically, the Slow Death has invested in the ways and means of war, nurturing death on a nation-state scale. Bodies of the dead were left on the ground, but also walking back to their homes to spread invisible death. Recently, Nergal and his sycophants have taken an interest in the sciences. Sowing doubt and misinformation among physicians and patients alike, they wrench rifts ever wider between those who would champion against infection and rot.

**Title** The Slow Death

**Areas of Concern** Atrocity, pestilence, war

**Edicts** Consume fungus and fermented or germinated foods, mutilate the dead, spread sickness

**Anathema** Deliberately smell a benign flower, use soap, burn or cremate the dead

**Religious Symbol** sun rising over battlefield

**Sacred Animal** jackal

**Sacred Colors** black, tan

**Source:** `= this.source` (`= this.source-type`)
