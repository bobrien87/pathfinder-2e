---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nosferatu Thrall"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +14, Deception +15, Religion +14"
abilityMods: ["+4", "+3", "+2", "+2", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "26; **Fort** +16, **Ref** +17, **Will** +14"
health:
  - name: HP
    desc: "135; **Weaknesses** mental 10"
abilities_mid:
  - name: "Fast Healing 5"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Mindbound"
    desc: "A nosferatu master exerts a fierce hold over their thrall's mind. If any creature other than the thrall's master targets them with an effect that would give them the [[Controlled]] condition, the thrall's master rolls a counteract check against it using their Dominate DC – 10 as the counteract check modifier."
  - name: "Rally"
    desc: "`pf2:r` **Trigger** The thrall ends their turn more than 30 feet away from their master <br>  <br> **Effect** The thrall Strides up to their Speed toward their master."
  - name: "Mortal Shield"
    desc: "`pf2:r` **Trigger** The thrall's master would take damage from a Strike or spell attack and is in an adjacent square <br>  <br> **Effect** The thrall throws themself in front of their master, taking half the damage of the attack (before applying any weaknesses or resistances). The thrall's master takes the remaining damage, applying any weaknesses or resistances as normal."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatclub +19 (`pf2:1`) (backswing, magical, shove), **Damage** 2d10+10 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +18 (`pf2:1`) (agile, nonlethal), **Damage** 2d6+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Swing Back"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** The nosferatu thrall's last action was a greatclub Strike that missed <br>  <br> **Effect** The nosferatu thrall makes another greatclub Strike against the same target, using the previous Strike's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Nosferatu thralls are mortals bound to a nosferatu's will. While thralls aren't undead, they stay alive by feeding on the blood of their masters.

Nosferatus are ancient vampires born of mortals who died in great plagues of old. Perhaps because of their old age, nosferatus can't create more of their kind.

```statblock
creature: "Nosferatu Thrall"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
