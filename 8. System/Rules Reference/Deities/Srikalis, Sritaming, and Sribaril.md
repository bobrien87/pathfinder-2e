---
type: deity
source-type: "Remaster"
domains: "Ambition, Passion, Perfection, Zeal"
favored-weapon: "Kris, Arquebus"
divine-font: "Harm"
divine-skill: "Society"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Haste]], Rank 5: [[Control Water]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

It is said that this triad of deities, known together as the Dewangayaw—Raiding God—sails the sea and sky upon a grand royal war barge. While they do not answer directly to the pleas of their followers and devotees, they very often appear at random, choosing to inflict violence upon those that deserve it. These events, known as god raids, are feared across Tian Xia. They can appear seemingly at random and are heralded by thunderstorms and sudden rains.

The Triad War Gods are the ancestors of the Tian peoples. They were the first warriors to roam the seas and lands of the archipelago and the great continent. They crafted the first war barges and sailed across the world. At the end of it, they realized the great lie of war: war is not needed, but violence must be inflicted. Violence is force and change, and The Triad understands violence must be used to reach Heaven. To force and change oneself is to turn oneself into a diamond. This philosophy is known to almost every warrior in Tian Xia: a concept they call Jamalawas, the Diamond Body, the act of perfecting one's body, spirit, and mind to become a better member of their community.

**Title** The Three-headed God of Raiding and War

**Areas of Concern** Raiding, treasure, war contracts, warriors

**Edicts** Die in battle, revel in protective violence, support what is yours

**Anathema** Lay waste to nature, kill indiscriminately without reason or conviction, choose not to raid when it is needed

**Religious Symbol** War barge with a flaming sail

**Sacred Animal** cat, monkey

**Sacred Colors** bronze, red

**Source:** `= this.source` (`= this.source-type`)
