---
type: deity
source-type: "Remaster"
domains: "Creation, Passion, Swarm, Wood"
favored-weapon: "Club"
divine-font: "Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Weave Wood]], Rank 2: [[Summon Elemental]], Rank 5: [[Plant Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Shumunue, Lord of Wood, is one of the few elemental lords not native to their plane of rule. Before the Carved Lady of Mimicry arrived on the Plane of Wood, it was a diverse and cultivated forest that stretched as far as the eye could see, yet it was eerily still. Animated creatures were rare, and beyond the wind through the boughs, little moved. Then Shumunue came to establish the Court of Transcendence. In her grotto, she taught the flowers and leaves to mimic praying mantises, bees, and moths. Then came herds of wooden deer, cranes, bats, and more, all delicately carved and polished. Within their minds, Shumunue imparted to these creatures the blueprints for their species and the instinct to carve their own descendants. Thus the Plane of Wood began to fill with life that resembled creatures from beyond its borders.

Some legends claim Shumunue is a construct who gained sentience for being universally perfect, but the Lady of Mimicry disputes this, stating that she's the product of a union between a kodama and a kizidhar wizard who traveled to her plane. She rules over no land or organization, for she sees no need to exert her personal opinions on anybody else. She instead dedicates herself to the act of creation. Rather than having subjects, the Carved Lady keeps a close group of confidants, who put in requests for her immense powers on behalf of others in need.

Shumunue maintains a sophisticated esca, or lure, of golden-hued wood. She regularly shaves this lure into the shape of a female humanoid with a head of ginkgo leaves. Some mistake this esca for Shumunue's physical form, but in actuality, the Carved Lady closely resembles an enormous forest dragon with scales like the bark of ancient trees. Her left flank bears a large blighted patch where Ayrzul's poison left its mark. While she's in no immediate danger, many on the Plane of Wood wait breathlessly to see whether their reconnection with the cosmos can cure her affliction.

**Title** The Carved Lady of Mimicry

**Areas of Concern** Camouflage, carpentry, life, mimicry, wood

**Edicts** Celebrate births, make time for nature, recreate life in your works

**Anathema** Permanently damage a plant or wood creature, polymorph another without permission

**Religious Symbol** carved wooden figurine with leaves for hair

**Sacred Animal** bagworm

**Sacred Colors** green, yellow

**Source:** `= this.source` (`= this.source-type`)
