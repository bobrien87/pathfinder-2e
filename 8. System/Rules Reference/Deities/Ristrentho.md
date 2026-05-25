---
type: deity
source-type: "Remaster"
domains: "Destruction, Freedom, Travel, Water"
favored-weapon: "Trident"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Liberating Command]], Rank 3: [[Aqueous Orb]], Rank 5: [[Elemental Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ristrentho, who appears as an otter with glittering scales, is popular with Sarkorian clans who fled down the Sellen River after the fall of Sarkoris. Today, their followers are eager to return to the banks of the Sarkora and West Sarkora Rivers. Ristrentho's worshippers are content to settle along watercourses, though most prefer to live a transient life on houseboats and water caravans. Though not always the most altruistic of people, followers of Ristrentho hold no truck with fiends and quickly send obvious villains on their way. Devotees of Ristrentho tend towards optimism and playfulness but also selfmotivation, carving their own course through the world like a wild river.

**Title** Whose Blood Churns

**Areas of Concern** Forward progress, removing barriers, rivers

**Edicts** Clear obstacles to progress, spend part of each day in motion

**Anathema** Dam a river or stream, hold a creature against its will

**Religious Symbol** twisting river

**Sacred Animal** otter

**Sacred Colors** blue, brown, gray

**Source:** `= this.source` (`= this.source-type`)
