---
type: deity
source-type: "Remaster"
domains: "Family, Introspection, Moon, Nature"
favored-weapon: "Longbow"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Ant Haul]], Rank 3: [[Earthbind]], Rank 7: [[Unfettered Pack]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Jukha is the goddess of big game hunting. She favors those who work together to bring down large beasts to feed their village, especially if they do so under the cover of night.

similar to Grask: she wanted to lead orcs into a new age of prosperity by changing how their neighboring countries viewed them. She planned to end the raids, unite the holds of Belkzen, and kill Tar-Baphon to prove her intentions. Despite being a teenager, Jukha gained a following through sheer physical prowess and ferocity, but she failed to inspire teamwork in her followers, and her group splintered. In frustration, she went on a solo hunt for a mammoth, but she and her prey simultaneously landed lethal blows. She and the mammoth breathed their last together and before she died, Jukha whispered her Deathright.

**Title** The Big Game Huntress

**Areas of Concern** Communal hunting, evening, feasts

**Edicts** Work together, push each other to greater heights, respect the animals you hunt

**Anathema** Abandon or betray your people, refuse to learn from your mistakes, isolate yourself

**Religious Symbol** crossed, bloody mammoth tusks

**Sacred Animal** wolf

**Sacred Colors** blue, green

**Source:** `= this.source` (`= this.source-type`)
