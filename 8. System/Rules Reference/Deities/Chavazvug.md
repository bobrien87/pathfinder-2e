---
type: deity
source-type: "Remaster"
domains: "Destruction, Dust, Fire, Pain"
favored-weapon: "War-flail"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 4: [[Wall Of Fire]], Rank 7: [[Volcanic Eruption]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Chavazvug is a towering mound of internal digestive organs supported by five long slender legs. Steam constantly rises from his grotesque body, and his touch can set creatures and objects ablaze. Chavazvug focuses on the destruction of demonkind. He appreciates the power of unholy fire to reduce even the most powerful enemies to mere dust. The Crawling Inferno has personally lead armies of his minions on invasions into demonic realms, knowing that, if slain, he can grow a new body from one of the many boiling lakes of bile within his cavernous realm.

**Title** The Crawling Inferno

**Areas of Concern** Demon hunters, fiery consumption, monstrous recursion

**Edicts** Commit arson, destroy demons, reduce your enemies to dust

**Anathema** Aid a demon, stop a fire from spreading

**Religious Symbol** burning tentacled rune

**Sacred Animal** none

**Sacred Colors** orange

**Source:** `= this.source` (`= this.source-type`)
