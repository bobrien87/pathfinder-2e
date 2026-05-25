---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Paleohemoth"
level: "12"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +20"
abilityMods: ["+7", "+2", "+6", "-5", "+0", "-5"]
abilities_top:
  - name: "Fossilization"
    desc: "The first time each round a creature takes damage from the paleohemoth's jaws, the target must attempt a DC 32 [[Fortitude]] save. If it fails and has not already been slowed by this ability, it becomes [[Slowed]] 1 for 1 minute. <br>  <br> If the creature was already slowed by this ability, a failed save causes it to be [[Petrified]] permanently."
armorclass:
  - name: AC
    desc: "33; **Fort** +26, **Ref** +20, **Will** +18"
health:
  - name: HP
    desc: "195; **Weaknesses** cold 10, earth 10, water 10; **Resistances** physical 10 except adamantine, bludgeoning, spells 10 except cold, earth, water"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +26 (`pf2:1`) (deadly d10, magical, reach 15 ft., unarmed), **Damage** 3d10 + 13 piercing plus [[Fossilization]]"
spellcasting: []
abilities_bot:
  - name: "Reassemble"
    desc: "`pf2:1` The paleohemoth reorganizes its bones, increasing its reach to 25 feet and reducing its Speed to 15 feet. It can revert to its original form by taking this action again."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Paleohemoths are typically made from the fossilized bones of dinosaurs and other ancient megafauna, though some crafters stretch the definition and instead use magically petrified bones of dragons or even giants. Not bound to any specific model, paleohemoths are crafted to be as terrifying as possible instead of models of anatomic accuracy. As such, most paleohemoths are nightmarish saurian amalgams whose massive arms end with the complete skulls of apex predators like tyrannosauruses, their bite enhanced to petrify flesh.

Intact fossilized bones are difficult components to scrounge, much less whole skeletons. An alternate way to obtain them is to hire expert hunters or adventurers to seek out live dinosaurs, bring back the bones, and use magic to turn them to stone. Of course, some purists prefer genuine fossilized bones and are willing to pay the price for their acquisition. Either way, opportunities await enterprising souls with the proper tools and several *spacious pouches*.

The magic that animates paleohemoths grants them a form of modular flexibility, letting them trade mobility for extended reach through the rapid rearrangement of their limbs. This often involves bones moving from the legs in order to extend the arms. While this does lead to a somewhat silly anatomy, it is nonetheless effective. This ability also lets them appear like a jumbled mass of bones at rest, making them likely to be mistaken for decor rather than guardians.

The reasons for creating such constructs vary. While they're often associated with guarding evil geniuses in deep, dark dungeons, they have great uses elsewhere. More elegant versions may be used to protect the private collections of upper-class collectors. Thuvia makes great use of paleohemoths in their construct arenas. While they weren't initially permitted to fight, an exploited loophole has made them a popular addition to the arenas ever since.

```statblock
creature: "Paleohemoth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
