---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hippogriff"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +7, Survival +6"
abilityMods: ["+3", "+3", "+2", "-4", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "32"
abilities_mid:
  - name: "Buck"
    desc: "`pf2:r` DC 17 [[Reflex]] save <br>  <br> Most monsters that serve as mounts can attempt to buck off unwanted or annoying riders, but most mounts will not use this reaction against a trusted creature unless the mounts are spooked or mistreated. <br>  <br> **Trigger** A creature [[Mounts]] or uses the [[Command an Animal]] action while riding the monster. <br>  <br> **Effect** The triggering creature must succeed at a Reflex saving throw against the listed DC or fall off the creature and land [[Prone]]. If the save is a critical failure, the triggering creature also takes 1d6 bludgeoning damage in addition to the normal damage for the fall."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +9 (`pf2:1`) (unarmed), **Damage** 1d10+3 piercing"
  - name: "Melee strike"
    desc: "Talon +9 (`pf2:1`) (agile, unarmed), **Damage** 1d6+3 slashing"
  - name: "Melee strike"
    desc: "Wing +9 (`pf2:1`) (reach 10 ft.), **Damage** 1d6+3 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Flying Strafe"
    desc: "`pf2:2` The hippogriff Flies up to its fly speed and makes two talon Strikes at any point during that movement. Each Strike must target a different creature. The attacks take the normal multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

With the proud bearing of a great raptor and the magnificence of a powerful horse, hippogriffs are thought to be an accidental fusion of creatures or perhaps the creation of a flesh-warping wizard with a keen aesthetic sense. Regardless of their original source, these animals are now a common sight in the skies above their favored plains or hill country.

Hippogriffs bear the wings, forelegs, and head of a bird of prey, with feather coloration similar to that of a hawk or eagle, though some breeders have managed to produce specimens with stark white or coal-black feathers. Their torso, hindquarters, and tail resemble those of a horse and usually are colored bay, chestnut, or gray, with some coats bearing black, pinto, or even palomino coloration.

Hippogriffs are similar in size to large horses. Much like their equine cousins, hippogriffs often have to keep wary eyes on the skies above them, as both are preferred meals for hungry griffons and wyverns. Only hippogriffs' superior speed helps protect them from these predators.

Hippogriffs are exceptionally territorial and fiercely protect the lands under their domain. They typically favor sweeping grasslands, rolling hills, and prairies. Exceptionally hardy hippogriffs make their homes nestled into niches on canyon walls, from which they comb the rocky deserts for coyotes, deer, and the occasional humanoid. Hippogriffs prefer mammalian prey, but they graze after every meal to aid in digestion.

Since hippogriff hunting habits can be dangerous to both ranchers and their livestock, such communities often set bounties on hippogriffs. As a result, preserved hippogriffs frequently decorate frontier taverns and remote outposts alongside the taxidermied remains of deer, elk, and bears.

However, other communities train hippogriffs from hatching to be ridden by elite soldiers in combat—the most notable among these groups in the Inner Sea region is the Sable Company Mercenaries in the city-state of Korvosa. Attempts are sometimes made to train adult hippogriffs in the same manner, but this often proves far more difficult. Hippogriff riders must use special saddles and combat techniques that allow them to act in concert with their mount, fighting effectively while avoiding interfering with the movement of their companion's wings.

```statblock
creature: "Hippogriff"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
