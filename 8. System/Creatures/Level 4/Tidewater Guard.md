---
type: creature
group: ["Humanoid", "Lizardfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tidewater Guard"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Lizardfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10"
languages: "Common, Iruxi"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +12, Nature +10, Stealth +11, Survival +10"
abilityMods: ["+4", "+3", "+1", "-1", "+2", "+0"]
abilities_top:
  - name: "Deep Breath"
    desc: "A tidewater guard can hold their breath for 20 minutes."
  - name: "Tethered Tridents"
    desc: "The tidewater guard's tridents are specially prepared to be aquadynamic and tethered by ropes. They have the tethered trait, meaning that a wielder who has a free hand can Interact to pull the weapon back into their grasp after they have thrown it as a ranged attack or after it has been disarmed (unless it is being held by another creature)."
  - name: "Terrain Advantage"
    desc: "Non-lizardfolk creatures that are in difficult terrain or are in water and lack a swim Speed are [[Off Guard]] to the tidewater guard."
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +11, **Will** +10"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trident +14 (`pf2:1`) (tethered), **Damage** 1d8+7 piercing"
  - name: "Melee strike"
    desc: "Trident +13 (`pf2:1`) (tethered, thrown 20), **Damage** 1d8+7 piercing"
  - name: "Melee strike"
    desc: "Claw +14 (`pf2:1`) (agile, unarmed), **Damage** 1d6+7 piercing"
spellcasting: []
abilities_bot:
  - name: "Reel In"
    desc: "`pf2:2` The tidewater guard makes a ranged Strike with their trident. If the Strike hits, the guard can haul on the attached line, moving the target up to 30 feet in a straight line toward the iruxi."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Iruxi tidewater guards are capable fighters skilled at amphibious attacks and overpowering vessels along any shore. Because lizardfolk settlements are typically constructed partially underwater and partially above, they have need of defenders who can guard from attacks in both environments.

The special spaulders tidewater guards wear set them apart from other lizardfolk warriors. These protect their shoulders from cutlass and axe strikes, and might be constructed of dragon scales, turtle or giant chiton shells, lacquered wood, or even sea urchin tests. The recipe for the special resin iruxi armorers apply to harden these spaulders is a closely guarded secret, and each iruxi community's supply of the resin is small, precious, and closely guarded.

Lizardfolk culture has flowered in recent years. With that revival has come a new generation of iruxis (as they call themselves) more willing to engage with the wider world, bringing with them their society's reverence for the past, facility with nature, and willingness to defend itself.

```statblock
creature: "Tidewater Guard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
