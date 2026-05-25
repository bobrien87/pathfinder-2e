---
type: creature
group: ["Fey", "Sprite"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pixie"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Fey"
trait_02: "Sprite"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Low-Light Vision]]"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +13, Deception +11, Nature +10, Stealth +11"
abilityMods: ["-1", "+5", "+1", "+3", "+2", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +8, **Ref** +14, **Will** +12"
health:
  - name: HP
    desc: "40; **Weaknesses** cold iron 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +13 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 1d6+4 piercing"
  - name: "Ranged strike"
    desc: "Longbow +13 (`pf2:1`) (deadly d10, magical, reload 0, volley 20, range 100 ft.), **Damage** 1d8+4 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 21, attack +13<br>**2nd** [[Dispel Magic]], [[Entangling Flora]], [[Invisibility (At Will, Self Only)]], [[Revealing Light]]<br>**1st** [[Detect Magic]], [[Figment]], [[Illusory Disguise]], [[Light]], [[Shield]]"
abilities_bot:
  - name: "Sprinkle Pixie Dust"
    desc: "`pf2:1` The pixie sprinkles pixie dust onto one of their arrows. If the pixie hits a creature with that arrow before the pixie's next turn, the arrow inflicts one of the following special effects of the pixie's choice instead of dealing damage. Each effect depends on the target's DC 21 [[Will]] save. On a critical hit, the target gets a result one degree worse than it rolled. <br>  <br> - **Charm** (emotion, incapacitation, mental) The arrow has the effect of a [[Charm]] spell, except the target doesn't gain a bonus to its save if the only hostile act was the pixie firing its bow, and the pixie can choose to direct the target's adoration toward another creature rather than itself. <br>  <br> - **Memory Loss** (mental) On a failed Will save, the target loses the last 5 minutes of its memory. <br>  <br> - **Sleep** (incapacitation, mental, sleep) The target suffers the effects of a 3rd-rank [[Sleep]] spell. <br>  <br> - **Subdual** (mental, nonlethal) The target takes 4d6 mental damage, depending on its basic Will save."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Insatiably curious, overly excitable, and just a bit puckish, pixies are wanderers and tricksters who use their pixie dust to create all sorts of whimsical situations, as well as to defend themselves. They take great pride in their skill at archery, even when not using their arrows to deliver magical ailments. They often practice by shooting drops of dew or severing vines and hairs. Other creatures often have trouble understanding a pixie's rapid, rambling way of speaking.

Elusive, flighty, and ebullient, sprites are what many villagers first imagine when they hear the terms "fey" or "fairy." While their dispositions vary, all sprites share a connection to magic and a diminutive size. This family of fey shares its name with its slightest and most populous member, the common sprite.

```statblock
creature: "Pixie"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
