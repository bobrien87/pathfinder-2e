---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ash Giant"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Low-Light Vision]]"
languages: "Common, Jotun"
skills:
  - name: Skills
    desc: "Athletics +24, Crafting +16, Diplomacy +16, Intimidation +21, Survival +21"
abilityMods: ["+7", "+3", "+6", "-1", "+4", "-2"]
abilities_top:
  - name: "Vermin Empathy"
    desc: "The ash giant can ask questions of, receive answers from, and use the Diplomacy skill with insects, arachnids, and similar creatures."
armorclass:
  - name: AC
    desc: "30; **Fort** +23, **Ref** +18, **Will** +21"
health:
  - name: HP
    desc: "240"
abilities_mid:
  - name: "+2 Status to All Saves vs. Disease"
    desc: ""
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Tumor Pop"
    desc: "When the ash giant takes piercing damage while they have a swollen tumor, the tumor explodes automatically, with the effect of Blastboil."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "War Flail +24 (`pf2:1`) (disarm, magical, reach 10 ft., sweep, trip), **Damage** 2d10+13 bludgeoning plus [[Gore Grinder]]"
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d4+13 bludgeoning"
  - name: "Ranged strike"
    desc: "Piggy Clod +24 (`pf2:1`) (brutal, range 40 ft.), **Damage** 2d8+7 slashing plus 5 slashing"
spellcasting: []
abilities_bot:
  - name: "Blastboil"
    desc: "`pf2:1` The ash giant pops one of the massive, swollen pustules on their body. Each creature in a @Template[type:cone|distance:15] takes @Damage[5d8[poison]|options:area-damage] damage with a DC 29 [[Reflex]] save. A creature that fails its save is also [[Sickened]] 1 (or [[Sickened]] 2 on a critical failure). This ability and tumor pop can't be used again until another tumor swells to a suitable size in 1d4 rounds."
  - name: "Gore Grinder"
    desc: "`pf2:1` **Requirements** The ash giant's last action was a successful war flail Strike <br>  <br> **Effect** The ash giant wraps the chain of the flail around the target and grinds its flesh. The creature takes @Damage[2d10[slashing],2d8[persistent,bleed]]{2d8 slashing damage and 2d8 persistent bleed damage} with a DC 30 [[Fortitude]] save."
  - name: "Tangle-Topple"
    desc: "`pf2:2` The ash giant makes a piggy clod Strike. If it hits, the target is tangled in ragged scrap. It's [[Immobilized]], can't leave the ground, and falls to the ground if it's flying. This ends if the creature Escapes or the metal is Forced Open."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Rugged and covered in pustules and sores from wandering harsh wastelands, ash giants dwell in the unwelcoming wilderness. Their lives are difficult, hardening them into utterly vicious, capricious, and cruel creatures. Their sadistic sense of humor and love for pranks makes them hated by almost all humanoids they encounter. Despite being crass and rough, ash giants are survivors above all, and they use their ingenuity to craft weapons, traps, harnesses for mounts, and tools. If the aim is cruelty, brutality, or a prank, an ash giant will find a way to craft the tools they need. Piggy clods are a favorite construction—contraptions of scrap iron and other metals rigged into a ball that explodes on impact.

Spread across the world, giants are as diverse as the isolated places they inhabit. A giant makes a big impression on the local environment, especially on smaller and weaker creatures.

```statblock
creature: "Ash Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
