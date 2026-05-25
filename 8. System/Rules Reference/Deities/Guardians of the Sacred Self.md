---
type: deity
source-type: "Remaster"
domains: "Change, Family, Protection, Soul"
favored-weapon: "Shield-boss"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Fleet Step]], Rank 3: [[Threefold Aspect]], Rank 4: [[Flicker]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Guardians of the Sacred Self understand something that many others do not: that what a person believes about themselves far outweighs that which others may judge them for. While individually they support the differences of their worshippers, these eleven deities and demigods have come together to become better advocates for change, empowering their followers to do the same. They strive for a world in which everyone can feel safe and secure being who they truly are.

**Pantheon Members** Alseta, Arazni, Cayden Cailean, Folgrit, Gozreh, Lalaci, Lymnieris, Matravash, Shelyn, Tsukiyo, Uvuko

**Areas of Concern** community building, community service, protecting the persecuted and downtrodden, raising awareness

**Edicts** empower, protect, and give aid to the disabled, those who deal with mental illness, and those who have transitioned to embrace their true selves

**Anathema** ignore genuine requests for help, make assumptions about others based on their appearance, take advantage of another's disability

**Religious Symbol** shield-shaped cocoon split down the middle

**Source:** `= this.source` (`= this.source-type`)
