---
type: creature
group: ["Construct", "Soulbound"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Soulbound Doll (Brave)"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Construct"
trait_02: "Soulbound"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "One Spoken by its Creator (typically Common)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Occultism +4, Stealth +8"
abilityMods: ["-2", "+4", "+3", "+0", "+2", "+0"]
abilities_top:
  - name: "Personality Fragments"
    desc: "A soulbound doll shares fragments of its donor soul's personality, though none of that creature's memories. This causes a soulbound doll to match a strong personality trait of the donor soul. Because of its soul sliver, a soulbound doll is not immune to spirit as most constructs are."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +10, **Will** +6"
health:
  - name: HP
    desc: "23; **Resistances** bludgeoning 3, piercing 5, slashing 3"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, magical, unarmed), **Damage** 1d6+2 bludgeoning"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 18, attack +10<br>**3rd** [[Levitate]]<br>**2nd** [[Enlarge]]<br>**1st** [[Light]], [[Prestidigitation]], [[Telekinetic Hand]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Soulbound dolls are eerie mannequins or playthings that have been imbued with a small piece of a deceased mortal's soul. These little constructs are created for a variety of reasons—such as to serve as companions or servants—but their free will means their obedience to their creators is hardly a given. Followers of Pharasma generally abhor soulbound dolls, viewing them as a perversion of the natural cycle of souls, and those who worship the Lady of Graves see the destruction of a soulbound doll, regardless of the construct's behavior, as an important service to the Great Beyond.

Soulbound dolls are the simplest in a series of soulbound constructs, including human-sized soulbound mannequins, powerful soulbound shells, and sentinel soulbound terra-cotta warriors. Creating them from unwilling living creatures is cruel, and an unwilling donor can resist the process with a successful Will save against the creator's Craft DC, ruining the doll if not preventing the donor's death. A doll can also be crafted from the soul of a person who has given consent to such use before their death.

Soulbound dolls encountered by adventurers are typically guardians of some sort; despite their diminutive size, the soul fragment's power makes the doll's fist more dangerous than a casual observer would expect. Further, it grants the doll a single spell of outsized power, given its stature. Because of their autonomy and remarkable intelligence, soulbound dolls are occasionally employed by their crafters as administrators over much more powerful but mindless constructs, allowing such dolls to control defenses far beyond their own capabilities.

Though soulbound dolls contain a small fragment of a soul extracted during or shortly after a person's death, this doesn't affect the deceased's resurrection or progress to the afterlife. This extraction process is typically lethal to otherwise living prospective soul donors.

The soul fragment resides in a soul focus gem (Hardness 10) typically embedded in the doll's neck or chest. The soul fragment generally clings to a strong personality trait of the original soul, but the doll continues to learn from its initial state, meaning its personality and abilities can change, possibly growing closer to the donor's or moving farther afield on its own individual path. The soulbound doll's focus gem retains the doll's memories even after the doll's destruction. The intact soul focus gem of a destroyed doll can even be placed into a new doll body by someone knowledgeable in the creation of soulbound creatures, effectively reconstituting the soulbound doll.

```statblock
creature: "Soulbound Doll (Brave)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
