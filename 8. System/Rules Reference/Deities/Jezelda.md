---
type: deity
source-type: "Remaster"
domains: "Destruction, Might, Moon, Trickery"
favored-weapon: "Claw, Scimitar"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Fleet Step]], Rank 2: [[Feral Shades]], Rank 5: [[Moon Frenzy]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Jezelda, the demon lord of desolation, the moon, and werewolves, is also known as the Mistress of the Hungry Moon. Legends claim she was the first lycanthrope, but neither she nor her followers have confirmed this. Jezelda is a patron specifically of werewolves, and she and her followers wage war against any non-werewolf werebeast. Her three forms consist of a dark-haired woman, a feral wolf with yellow eyes, and an emaciated combination of the two. Cultists form around two types of hunts. In the first, the cultists find someone worthy of Jezelda's blessing, stalk them for one moon cycle, and then hunt them down together to turn them into a werewolf. In the other type, the cultists find an individual worthy of sacrifice, stalk them for a year, and then hunt them down to kill them. Their success or failure determines if they have won or lost Jezelda's favor for that year. Over time, these deaths and forced conversion to lycanthropy can turn communities into ghost towns.

**Title** Mistress of the Hungry Moon

**Areas of Concern** Desolation, the moon, werewolves

**Edicts** Eat raw meat and blood, hunt on the night of the full moon, prey on the weak and defenseless

**Anathema** Betray your pack, offer succor to nonwerewolf shapeshifters, use silver as a weapon

**Religious Symbol** full moon above moor

**Sacred Animal** wolf

**Sacred Colors** black, silver

**Source:** `= this.source` (`= this.source-type`)
