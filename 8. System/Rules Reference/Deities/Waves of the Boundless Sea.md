---
type: deity
source-type: "Remaster"
domains: "Fate, Repose, Travel, Water"
favored-weapon: "Trident"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 3: [[Aqueous Orb]], Rank 5: [[Control Water]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Life-giving water is an important building block for most civilizations. It's needed to fill wells, irrigate farms, and facilitate the movement of goods. It's the reason many of the world's most prosperous cities are built on coasts and riverbanks. Many find this fact worthy of reverence, but don't wish to pay obeisance to any particular ocean or river god. They put their faith in the water itself, often personified in spirits and elementals of the Plane of Water. Followers of the Waves of the Boundless Sea also respect the sheer power of the ocean and the ceaseless but ultimately predictable tides. Many go through life drifting on the currents of fate, letting circumstances carry them like a river to the sea. Others understand that while waves might toss and capsize a ship, water not tossed by the winds should be more calming and regularly bathe or soak themselves for therapeutic purposes.

**Covenant Members** faydhaans, the Plane of Water, sea serpents, spirits of water, water elementals

**Areas of Concern** aquatic creatures, currents, swimming, tides, water

**Edicts** allow the currents of life take you where they may, travel the expansive seas, wash away dust and dirt with seawater

**Anathema** allow a creature to drown when you could save them, toss detritus into the oceans

**Religious Symbol** crashing wave

**Source:** `= this.source` (`= this.source-type`)
