---
type: deity
source-type: "Remaster"
domains: "Decay, Indulgence, Nature, Passion"
favored-weapon: "Sickle"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Charm]], Rank 4: [[Suggestion]], Rank 5: [[Plant Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Eldest of carnivorous plants, intrigue, and seduction, the Green Mother personifies the raw thrill and desire found throughout nature. Lush plants that entice prey only to kill with barbs or toxins lie within her authority, as do lustful acts and whispered secrets occurring in wild terrain. Her seductive form shifts from that of a beautiful fey such as a nymph to incorporating natural lures like sweet-smelling flowers and graceful verdant tresses. Just as the Green Mother's form constantly changes, her mood shifts from mercurial temptress to indifferent poisoner. No matter her form or attitude, the Green Mother is among the canniest of the Eldest, and she maintains several loyal agents who keep her well informed about goings-on in the First World and beyond. This information fuels her intrigues among the Eldest, and they all believe it wisest to keep on the Green Mother's good side lest their secrets be seductively whispered into the ears of their enemies.

**Title** The Feasting Flower

**Areas of Concern** Carnivorous plants, intrigue, seduction

**Edicts** Frolic in vegetation, manipulate people, use what you kill, prey on the weak

**Anathema** Hold a secret for too long, discriminate against sex workers or use their trade to harm them

**Religious Symbol** briar-wrapped lips

**Sacred Animal** none (plants)

**Sacred Colors** green, red

**Source:** `= this.source` (`= this.source-type`)
