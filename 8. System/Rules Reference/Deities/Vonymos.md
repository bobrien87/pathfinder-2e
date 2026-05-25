---
type: deity
source-type: "Remaster"
domains: "Death, Destruction, Sorrow, Zeal"
favored-weapon: "Scythe"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Endure]], Rank 3: [[Blazing Dive]], Rank 8: [[Falling Sky]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Grief is a powerful emotion, felt by every mortal in every lifetime, and from the pain of intense loss crashing through mortal hearts a psychopomp usher was born: Vonymos, the Mourning Storm. They embody all that grows from a heart in mourning, both good and ill. They are depression, isolation, and desperation, but they are also last stands against the dark, renewed vigor, and hope. The usher's touch is felt when emotions swell, building up until they grow too overwhelming to contain, when the walls within crumble and the flood is unleashed. They are the crack of lighting that pushes mortals through despair, igniting the inner fire needed to make a final, desperate rally before succumbing to defeat. They are the usher of catastrophes, of last stands, and of suicides.

**Title** The Mourning Storm

**Areas of Concern** Catastrophes, last stands, suicides

**Edicts** Aid the depressed, comfort the grieving, experience and act on intense emotions

**Anathema** Attempt to regulate others' emotions, dismiss or mock a creature's suffering, surrender without a fight

**Religious Symbol** hollow circle with three trailing lines curling clockwise from it

**Sacred Animal** swan

**Sacred Colors** black

**Source:** `= this.source` (`= this.source-type`)
