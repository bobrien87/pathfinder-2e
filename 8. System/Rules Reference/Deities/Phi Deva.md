---
type: deity
source-type: "Remaster"
domains: "Family, Healing, Protection, Repose"
favored-weapon: "Shortbow"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Soothe]], Rank 4: [[Flicker]], Rank 7: [[Project Image]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Made of a thousand nameless faces and a thousand nameless voices, Phi Deva speaks for and defends those who can't protect themselves. They are both one god and a thousand, both mortal and yet infinite. The Thousand Souled Chorus is neither a god of a single soul nor a mortal who ascended the heights to godhood, for that would imply they rose out of exceptionable mortality. Instead, they are a god borne of blood, sweat, and death, of the defenseless who were not protected and now seek to protect those who can't protect themselves. Phi Deva is most often worshipped by the common people, though anyone who seeks their protection is welcomed into the chorus. But powerful figures beware, for bringing the sights of the Chorus onto oneself can be dangerous for those who do not check their own power.

**Title** The Thousand-souled Chorus

**Areas of Concern** People, the defenseless, the collective good

**Edicts** Protect the defenseless, assist those who ask for your help, put the collective above yourself

**Anathema** Harm the innocent, take more than you need, overturn a collective decision

**Religious Symbol** Bird protecting a second, lifeless bird

**Sacred Animal** sparrow

**Sacred Colors** all

**Source:** `= this.source` (`= this.source-type`)
