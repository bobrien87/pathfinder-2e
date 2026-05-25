---
type: creature
group: ["Caligni", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Caligni Vanguard"
level: "5"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Caligni"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Echolocation]] (precise) 60 feet"
languages: "Caligni, Sakvroth"
skills:
  - name: Skills
    desc: "Athletics +14, Stealth +8"
abilityMods: ["+5", "-1", "+3", "+1", "+4", "+1"]
abilities_top:
  - name: "Echolocation 60 feet"
    desc: "A caligni vanguard can use their hearing as a precise sense at the listed range."
armorclass:
  - name: AC
    desc: "24; **Fort** +14, **Ref** +8, **Will** +11"
health:
  - name: HP
    desc: "50; death blaze; **Immunities** visual; **Weaknesses** sonic 5; **Resistances** slashing 5"
abilities_mid:
  - name: "Death Blaze"
    desc: "When the vanguard dies, their body combusts in a blaze of fire and armor shrapnel. All creatures within a @Template[emanation|distance:10] take @Damage[3d6[fire],3d6[piercing]|options:area-damage]{3d6 fire damage and 3d6 piercing damage} (DC 19 [[Reflex]] save). The vanguard's armor is destroyed in the blaze, but their other gear is unaffected and left in a pile where they died."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatsword +16 (`pf2:1`) (versatile p), **Damage** 1d12+8 slashing"
  - name: "Ranged strike"
    desc: "Composite Longbow +10 (`pf2:1`) (deadly d10, volley 30, range 100 ft.), **Damage** 1d8+5 piercing"
spellcasting: []
abilities_bot:
  - name: "Call to Arms"
    desc: "`pf2:1` Each caligni within @Template[emanation|distance:30]{30 feet} of the vanguard gains the [[Reactive Strike]] reaction until the end of the vanguard's next turn. Once a caligni has used this Reactive Strike, that caligni is temporarily immune to the same vanguard's Call to Arms for 10 minutes."
  - name: "Shadowed Blade"
    desc: "`pf2:2` The vanguard makes a melee Strike, channeling shadowy essence into their weapon or unarmed attack to envelop the target. If the Strike hits, the target must succeed at a DC 19 [[Fortitude]] save or become [[Blinded]] until the end of its next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Caligni children born without eyes-an extremely rare occurrence-are considered sacred to their communities. From a young age, they're set aside and groomed to become caligni vanguards, dedicated to rigorous martial training and mental strictures. Other calignis revere vanguards' discipline and combat skill, but wary caution always tinges such respect, as they often have inscrutable motives. Vanguards almost never rebel against their duties or their established role in the community; some claim that those who do are taken by the owbs.

A vanguard's armor is fused to their body in pieces, and they rarely remove those elements that aren't. This armor plating and vanguards' keen sense of hearing render them particularly sensitive to sonic vibrations, which serves as both an asset and a vulnerability.

Each individual in caligni society serves a specific role. At times, certain roles so rarely find suitable candidates that a community might only see a few individuals fill them in an entire generation.

```statblock
creature: "Caligni Vanguard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
