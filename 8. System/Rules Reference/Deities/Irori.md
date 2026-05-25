---
type: deity
source-type: "Remaster"
domains: "Knowledge, Might, Perfection, Truth"
favored-weapon: "Fist"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Jump]], Rank 3: [[Haste]], Rank 4: [[Mountain Resilience]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

As a mortal, Irori attained true enlightenment, allowing him to break free of the shackles of mortality and achieve divinity. As a god, he is the Master of Masters and promotes discipline and teaches that one who can master themself finds the greatest benefits the world can provide.

**Title** Master of Masters

**Areas of Concern** history, knowledge, self-perfection

**Edicts** be humble; help others perfect themselves; hone your body, mind, and spirit to a more perfect state; practice discipline

**Anathema** destroy an important historical text, engage in overly unhealthy or self-destructive behaviors, repeatedly fail to maintain self-control

**Divine Symbol** blue hand

**Sacred Animal** snail

**Sacred Colors** blue, white

**Source:** `= this.source` (`= this.source-type`)
