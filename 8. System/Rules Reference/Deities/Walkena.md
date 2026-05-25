---
type: deity
source-type: "Remaster"
domains: "Family, Freedom, Sun, Tyranny"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 3: [[Fireball]], Rank 4: [[Wall Of Fire]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In the city-state of Mzali in the Mwangi Expanse resides an undead being of immense power, a child-sized god-king. In the past, Walkena was a mortal descendant of the gods that ruled over Mzali in ancient times, one of the sun kings from an old empire and a golden age of the city. Ages later, his preserved body was found by members of the Council of Mwanyisa, who ruled Mzali at that time. Believing him to be an omen of the city's impending resurgence, the council took him to put him on display in Mzali. When an army from the Sargavan city of Kalabuto attacked the city, Walkena awoke-this time as an undead creature-and slew each of the invaders in a purging rain of fire.

**Title** The God-King

**Areas of Concern** Mzali, nationalism, reverence

**Edicts** Uphold Mzali's laws, tend to Walkena and obey his instructions, oppose exploitation of the Mwangi Expanse

**Anathema** Consort or trade with non-Mwangi peoples, defy Walkena's orders

**Religious Symbol** Lion-faced sun shining on Walkena

**Sacred Animal** lion

**Sacred Colors** red, gold

**Source:** `= this.source` (`= this.source-type`)
