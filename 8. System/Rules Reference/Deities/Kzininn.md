---
type: deity
source-type: "Remaster"
domains: "Nature, Protection, Pain, Wood"
favored-weapon: "Spiked-chain"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Goblin Pox]], Rank 2: [[Blood Vendetta]], Rank 3: [[Wall Of Thorns]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In an ancient, more carefree age, Kzininn guided the growth of succulents, ferns, and other lush plants. This idyllic existence ended when Desna discovered Ghlaunder, unleashing that parasitic god upon the multiverse. Like a legion of aphids, Ghlaunder fell upon Kzininn, draining his fluids and vitality until only a withered husk remained. When he was sated and flew to seek other prey, Kzininn wasn't quite dead, but he was angry.

Over time, he regrew. Where once there was soft flesh, waxy cuticles took shape. Rounded leaves gave way to menacing thorns. The sweet sap became bitter with toxins. Kzininn remained a guardian of nature, yet he had rebuilt himself into a bristling juggernaut.

Since then, Kzininn has championed cacti, brambles, nightshades, and other hazardous plants, encouraging flora to evolve defenses so that they don't fall prey to remorseless fauna. His followers often seed nettles to ward off grazers from vulnerable undergrowth. Worshippers incorporate small spines into their attire, and although intimacy isn't discouraged, the faithful are expected to exercise healthy physical and social boundaries.

Kzininn's realm winds through the Shattered Peaks of western Nex and Katapesh, spilling into parts of the Mwangi Expanse. He is reclusive, rarely revealing himself but instead encouraging his wards to develop increasingly deadly—if not outright carnivorous—defenses. It seems Kzininn views the cultivation of pesh cacti in Katapesh with particular disdain; his disciples occasionally liberate or even animate the cacti to revolt, tearing apart their farmers to water the soil with blood.

**Title** The Prince of Thorns

**Areas of Concern** Dangerous plants, boundaries, harsh lessons

**Edicts** Equip the weak to defend themselves, preserve areas of natural wilderness, confront those who trespass and despoil, embrace scars

**Anathema** Allow flagrant abuse of plant life to go unpunished, prune a plant's natural defenses, fully heal wounds inflicted by plants

**Religious Symbol** budding flower growing from a wound

**Sacred Animal** leafcutter ant

**Sacred Colors** green, red

**Source:** `= this.source` (`= this.source-type`)
