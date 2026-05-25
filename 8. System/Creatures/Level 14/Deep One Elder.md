---
type: creature
group: ["Amphibious", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Deep One Elder"
level: "14"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Amphibious"
trait_02: "Humanoid"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Darkvision]], [[Wavesense]] (imprecise) 120 feet"
languages: "Aklo, Common"
skills:
  - name: Skills
    desc: "Athletics +31, Intimidation +24, Religion +27, Survival +25, Dagon Lore +24, Ocean Lore +24"
abilityMods: ["+9", "+4", "+8", "+6", "+5", "+4"]
abilities_top:
  - name: "Pressurized"
    desc: "A deep one is immune to damage and other negative effects from changes in water pressure."
  - name: "Devastation"
    desc: "A deep one elder's claw Strikes ignore the first 10 Hardness of an object. Additionally, on a critical hit, the target must succeed at a DC 34 [[Fortitude]] save or be [[Stunned]] 2."
armorclass:
  - name: AC
    desc: "36; **Fort** +27, **Ref** +22, **Will** +26"
health:
  - name: HP
    desc: "260; **Immunities** cold; **Resistances** acid 10, piercing 15"
abilities_mid:
  - name: "Endless"
    desc: "A deep one doesn't age and is immune to spells and other effects that inflict magical aging. Unless killed, a deep one lives forever."
  - name: "Frightful Presence"
    desc: "60 feet. DC 31 [[Will]] save. <br>  <br> A creature that fails its save is also [[Slowed]] 1 ([[Slowed]] 2 on a critical failure). <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Mental Mirror"
    desc: "Mental effects that fail against a deep one elder are reflected back onto the source, as [[Spell Riposte]]."
  - name: "Improved Knockdown"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature as a free action. This attempt neither applies nor counts toward the monster's multiple attack penalty."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Foot +29 (`pf2:1`) (magical, reach 20 ft., unholy), **Damage** 3d12+15 bludgeoning"
  - name: "Melee strike"
    desc: "Claw +29 (`pf2:1`) (agile, magical, reach 20 ft., sweep, unholy), **Damage** 3d10+12 slashing plus [[Devastation]] plus [[Improved Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, foot, DC 31 [[Reflex]] save <br>  <br> The deep one can Swim up to double its swim Speed instead of Striding. <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Watery Void"
    desc: "`pf2:3` The deep one elder makes an endless void of water appear in a @Template[type:burst|distance:20] within 60 feet, dragging creatures down into its whirlpool. If cast underwater, the watery void fills a 60-foot-tall cylinder with a 20-foot radius. Creatures in the area when the void appears and creatures that end their turn in the area take @Damage[3d8[bludgeoning]|options:area-damage] damage and @Damage[3d8[void]|options:area-damage] damage and must attempt a DC 31 [[Reflex]] save. The void remains until the end of the deep one elder's next turn. The deep one elder can Sustain the void to extend the duration by 1 round, up to a total of 4 rounds, and can move the void up to 15 feet. Once the effect ends, the elder can't use Watery Void again for 1d4 rounds. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature takes half damage and a –5-foot circumstance penalty to their Speeds while in the void. <br> - **Failure** The creature takes full damage and a –10-foot circumstance penalty to their Speeds while in the void. <br> - **Critical Success** The creature takes double damage, is knocked [[Prone]], and takes a –10-foot circumstance penalty to their Speeds while in the void."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Given enough time, deep one elders can swell to dizzying heights.

Lumbering, amphibious, and deathless humanoids known as deep ones inhabit coastal areas and deep ocean trenches all across Golarion. Though most simply wish to be left alone, others work tirelessly to grow their ranks.

```statblock
creature: "Deep One Elder"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
