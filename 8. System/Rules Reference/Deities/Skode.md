---
type: deity
source-type: "Remaster"
domains: "Ambition, Confidence, Protection, Zeal"
favored-weapon: "Longbow"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Vanishing Tracks]], Rank 3: [[Haste]], Rank 4: [[Weapon Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Skode, the daughter of Tjasse, is the huntress goddess of giants. She is portrayed as a stout and muscular cloud giant woman with her face and arms decorated with intricate tattoos, dressed in leathers and furs. She is well-known for her skills with a longbow and spear, and her intolerance for evil. Skode is wed to Aegirran, her might and passion having won his heart, but is separated from him by land and sea. The two are only ever able to embrace one another on the changing of seasons. For the remainder of the year, she forever stalks the land with the three sons she had with Aegirran (the bitter north winds), hunting the finest animals while seeking to destroy the wicked with arrows or spears aimed true. Like Fandarra and Bergelmir, she is one of the few giant deities who have a significant following of non-giants as well, largely among the Kellid people in the Realm of the Mammoth Lords.

**Title** The Horizon Huntress

**Areas of Concern** Heroism, hunting, pride, tracking, trophies

**Edicts** Take the finest or healthiest specimen among any animals you hunt, respect your prey, protect your community, show bravery in the face of danger

**Anathema** Waste the animals you hunt, show cruelty to animals, abandon your community in a time of danger

**Religious Symbol** sun rising over ocean

**Sacred Animal** osprey

**Sacred Colors** blue, yellow

**Source:** `= this.source` (`= this.source-type`)
