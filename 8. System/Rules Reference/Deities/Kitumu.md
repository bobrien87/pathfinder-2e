---
type: deity
source-type: "Remaster"
domains: "Destruction, Indulgence, Nightmares, Swarm"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Sleep]], Rank 2: [[Vomit Swarm]], Rank 3: [[Insect Form]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

If any fervent devotees of the monstrous firefly goddess exist, they don't venture into civilization. The closest Kitumu has to servants or worshipers are those willing to placate the goddess in order to satisfy her demands and hungers.

**Title** Mother of Fireflies

**Areas of Concern** Fireflies, hibernation, swarms

**Edicts** Offer sacrifices to Kitumu, feed the hungers of nature with humanoid creatures

**Anathema** step on a firefly, kill those marked by Kitumu

**Religious Symbol** four-legged firefly

**Sacred Animal** firefly

**Sacred Colors** black, yellow

**Source:** `= this.source` (`= this.source-type`)
