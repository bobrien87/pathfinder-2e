---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rune Giant"
level: "16"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+28; [[Low-Light Vision]]"
languages: "Common, Jotun, Petran"
skills:
  - name: Skills
    desc: "Arcana +28, Athletics +32, Crafting +28, Intimidation +28, Society +27"
abilityMods: ["+9", "+2", "+7", "+2", "+6", "+4"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Command Giants"
    desc: "When a rune giant casts a mental spell against another giant, the DC is 39, rather than 35"
armorclass:
  - name: AC
    desc: "38; **Fort** +33, **Ref** +26, **Will** +28"
health:
  - name: HP
    desc: "330; **Immunities** fire"
abilities_mid:
  - name: "Reactive Strike (Special)"
    desc: "`pf2:r` The rune giant gains an additional reaction at the beginning of each of their turns that they can use only for a Reactive Strike. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Flashing Runes"
    desc: "`pf2:0` **Trigger** The rune giant uses an arcane ability or casts an arcane spell <br>  <br> **Effect** The runes on the giant's body flash with magical energy. Each creature within a @Template[emanation|distance:10] must attempt a DC 35 [[Fortitude]] save. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Dazzled]] for 1 round. <br> - **Failure** The creature is [[Blinded]] for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatsword +33 (`pf2:1`) (magical, reach 20 ft., versatile p), **Damage** 3d12+17 slashing"
  - name: "Melee strike"
    desc: "Longspear +32 (`pf2:1`) (magical, reach 25 ft.), **Damage** 2d8+17 piercing"
  - name: "Melee strike"
    desc: "Fist +31 (`pf2:1`) (agile, reach 20 ft., unarmed), **Damage** 3d8+17 bludgeoning"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 35, attack +27<br>**6th** [[Dominate]], [[Truesight]]<br>**5th** [[Sending]]<br>**4th** [[Fly]] (Constant), [[Suggestion]], [[Suggestion]] (At Will)<br>**1st** [[Charm]], [[Charm]] (At Will)"
abilities_bot:
  - name: "Demand"
    desc: "`pf2:0` When a rune giant casts their innate [[Sending]] spell, they can also cast [[Suggestion]] on the target."
  - name: "Invoke Rune"
    desc: "`pf2:1` The rune giant invokes one of the runes on their body, causing the rune to spray forth a @Template[cone|distance:30] of sparks that deals @Damage[6d12[electricity]|options:area-damage] damage to all creatures in the cone (DC 37 [[Reflex]] save). <br>  <br> The giant can't use Invoke Rune again for 1d4 rounds. <br>  <br> A glowing copy of the invoked rune appears on a single weapon the giant holds, granting the weapon one effect listed below of the giant's choice. The effect on the weapon lasts for 1 minute. If the giant places a new rune on a weapon, any previously placed rune immediately vanishes, ending its effect. <br>  <br> - **Rune of Destruction** The weapon gains the deadly trait with three weapon damage dice of the same die size as for the base weapon, and a creature hit with the weapon is [[Drained]] 1 unless it succeeds at a DC 35 [[Fortitude]] save. <br>  <br> - **Rune of Flames** The weapon deals an additional 3d6 fire damage on all attacks. <br>  <br> - **Rune of Smiting** When the weapon hits, the giant can Push the target back 10 feet, or 20 feet on a critical hit. <br>  <br> - **Rune of Space** During the rune giant's turn, the weapon's reach is increased to 60 feet."
  - name: "Wide Swing"
    desc: "`pf2:1` The rune giant makes a single greatsword Strike and compares the attack roll result to the ACs of up to two foes within their reach. This counts as two attacks for the giant's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Rune giants are tyrants among their own kind, given power to command and magically control other giants. They once served even more powerful masters—potent wizards known as runelords—and in so doing, commanded entire armies of giants in service to the runelords' empires.

In the eons since these empires collapsed, rune giants have persisted, though to the outside world they're little more than fabled horrors. Rune giants usually dwell in the most remote and rugged of towering mountain ranges, but they can also be found in immense ruins atop lost islands, glacial valleys, or even more remote or magical regions.

Dozens of runes decorate rune giants' striking charcoal flesh. They are towering creatures, averaging at 40 feet in height and weighing 25,000 pounds.

Giants are massive humanoid creatures who live in remote regions throughout the world. They vary widely but are united in their hunger, requiring sustenance of their own element along with the feasts one would expect from such a massive humanoid. Although a simple matter for some giants, more esoteric types find this need a harsh reality. While a massive fistful of ice or snow alongside their meal will satisfy a frost giant, shadow giants hunger for the coagulated shadows of the Netherworld.

```statblock
creature: "Rune Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
