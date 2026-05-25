---
type: deity
source-type: "Remaster"
domains: "Decay, Healing, Nature, Wood"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Flourishing Flora]], Rank 2: [[Oaken Resilience]], Rank 5: [[Nature'S Pathway]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

With the Elemental Plane of Wood regaining prominence, some have turned to worshipping the life-giving force of the plane itself, alongside nature spirits that dwell in forests and other wooded areas. Followers of this covenant respect the cycle of rebirth that occurs in the blossoming of flowers every spring and the fungi that often grow from the decay of other living things. They also appreciate the many different ways that wood can be used in crafting, believing a finely carved piece of furniture to be akin to a work of art. Devotees of the Blooms of the Spreading Weald who live in urban areas of stone and metal, though rare, usually keep window box planters full of tiny shrubs or petition the local government to construct neighborhood gardens. Certain druidic enclaves of this covenant fight tirelessly against unscrupulous lumber consortia that clear-cut forests without any regard to the surrounding ecosystems.

**Covenant Members** forest and fungus spirits, kizidhars, the Plane of Wood, spirits of wood, wood elementals

**Areas of Concern** carpentry, fertility, fungi, plants, wood

**Edicts** encourage natural growth even in urban areas, expertly craft wooden furniture and other items, fight against blight

**Anathema** exploit natural resources such as timber, use herbs and fungi to make deadly poisons

**Religious Symbol** blossoming tree

**Source:** `= this.source` (`= this.source-type`)
