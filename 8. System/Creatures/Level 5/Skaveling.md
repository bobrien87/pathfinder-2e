---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skaveling"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]], [[Echolocation]] (precise) 40 feet"
languages: "Aklo, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +13, Intimidation +11"
abilityMods: ["+6", "+4", "+2", "+1", "+6", "+2"]
abilities_top:
  - name: "Echolocation"
    desc: "A skaveling can use their hearing as a precise sense at the listed range."
armorclass:
  - name: AC
    desc: "22; **Fort** +11, **Ref** +13, **Will** +15"
health:
  - name: HP
    desc: "80; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed"
abilities_mid:
  - name: "Feast on Fear"
    desc: "`pf2:r` **Trigger** The skaveling deals damage to a [[Frightened]] creature with a fangs Strike <br>  <br> **Effect** The skaveling draws power from the fear infusing a creature's flesh. The frightened creature must attempt a DC 22 [[Fortitude]] save saving throw. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature takes a –5-foot status penalty to its Speed, and the skaveling gains a +5-foot status bonus to their Speeds until the end of their next turn. <br> - **Failure** The creature takes a –10-foot status penalty to its Speed, and the skaveling gains a +10-foot status bonus to their Speeds until the end of their next turn. <br> - **Critical Failure** The creature is [[Slowed]] 1, and the skaveling can immediately Fly, Step, or Stride as a free action; this movement doesn't trigger reactions. <br>  <br> > [!danger] Effect: Feast on Fear"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +15 (`pf2:1`), **Damage** 2d8+8 piercing"
  - name: "Melee strike"
    desc: "Wing +15 (`pf2:1`) (agile), **Damage** 2d4+8 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Bone-Chilling Screech"
    desc: "`pf2:2` The skaveling unleashes a horrifying screech that chills the very bones of those close enough to feel it. The screech can be heard for miles, but each creature in a @Template[emanation|distance:20] must also attempt a DC 22 [[Will]] save. <br>  <br> The skaveling can't use Bone-Chilling Screech again for 1d4 rounds. <br> - **Critical Success** The creature is unaffected and is temporarily immune to Bone-Chilling Screech for 24 hours. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is frightened 2 and [[Stunned]] 1 by fear."
  - name: "Consume Flesh"
    desc: "`pf2:1` **Requirements** The skaveling is adjacent to the corpse of a creature that died within the last hour <br>  <br> **Effect** The skaveling devours a chunk of the corpse and regains 1d6 Hit Points plus 1d6 for every 2 levels the skaveling has (@Damage[(1+(max(0,floor(@actor.level/2))))d6[healing]]). They can regain Hit Points from any given corpse only once."
  - name: "Swift Dart"
    desc: "`pf2:1` The skaveling Flies up to half their Speed. This movement doesn't trigger reactions."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

One must perform a hideous ritual to make a skaveling. Though sometimes called ghoul bats, they're specifically crafted undead rather than true ghouls. The bloodsucking urdefhans of the Darklands raise giant bats on a toxic fungus and the flesh of ghouls—specifically their brains. Upon reaching maturity, these giant bats are ritually slain via poison. While this rots away the flesh of most creatures, the specially prepared bats immediately rise from death as skavelings.

Despite their tattered wings and sagging skin, skavelings are quite capable of flight, even when carrying a creature on their back. Urdefhans often use them as mounts. Their intelligence is more advanced than that of a typical giant bat, and in combat they behave more like allies than animals, capable of making tactical decisions.

```statblock
creature: "Skaveling"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
