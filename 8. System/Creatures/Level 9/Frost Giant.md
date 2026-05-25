---
type: creature
group: ["Cold", "Giant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Frost Giant"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Cold"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Low-Light Vision]]"
languages: "Common, Jotun"
skills:
  - name: Skills
    desc: "Athletics +23, Crafting +18, Intimidation +18, Nature +17, Stealth +17"
abilityMods: ["+6", "+0", "+5", "+0", "+2", "+0"]
abilities_top:
  - name: "Ice Stride"
    desc: "A frost giant isn't impeded by difficult terrain caused by snow or ice, nor do they need to attempt Acrobatics checks to keep from falling on slippery ice."
armorclass:
  - name: AC
    desc: "29; **Fort** +23, **Ref** +16, **Will** +16"
health:
  - name: HP
    desc: "150; **Immunities** cold; **Weaknesses** fire 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greataxe +21 (`pf2:1`) (magical, reach 10 ft., sweep), **Damage** 2d12+12 slashing"
  - name: "Melee strike"
    desc: "Fist +21 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d8+12 bludgeoning"
  - name: "Ranged strike"
    desc: "Icicle +21 (`pf2:1`) (cold, primal), **Damage** 3d6 cold plus 2d8 piercing"
spellcasting: []
abilities_bot:
  - name: "Chill Breath"
    desc: "`pf2:1` The frost giant breathes out a @Template[cone|distance:15] of freezing moisture that quickly condenses into ice, dealing @Damage[4d6[cold]|options:area-damage] damage. Each creature in the cone must attempt a DC 28 [[Reflex]] save. A creature that fails its save is also [[Immobilized]] and takes 2d6 cold damage at the end of each of its turns until it gets free (`act escape dc=28`). <br>  <br> The giant can't use Chill Breath again for 1d4 rounds."
  - name: "Wide Swing"
    desc: "`pf2:1` The frost giant makes a single greataxe Strike and compares the attack roll result to the ACs of up to two foes within their reach. This counts as two attacks for the frost giant's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Frost giants are remorseless marauders who pillage and plunder from those who dare to live near them in desolate, frigid lands. Their clans range from extremely territorial hunters who ferociously defend their expanse of tundra to nomadic families that roam icy slopes in search of settlements to conquer. Frost giant clans are ruled by the family member who exhibits the greatest ferocity and prowess in battle—often a massive bully who demands absolute obedience from the rest.

Frost giants' appearance is reflective of their icy homes, with flesh ranging from a translucent glacial blue to a slushy gray. A typical frost giant stands about 15 feet tall and weighs approximately 2,800 pounds. They often wear metal armor adorned with the furs, skin, teeth, and tusks of slain beasts and heft weapons as long as dining tables. A well-stocked frost giant clan will raise mammoth mounts or press witchwargs into service as hunting companions, but consider their environment too hostile for a soft concept like pets.

Giants are massive humanoid creatures who live in remote regions throughout the world. They vary widely but are united in their hunger, requiring sustenance of their own element along with the feasts one would expect from such a massive humanoid. Although a simple matter for some giants, more esoteric types find this need a harsh reality. While a massive fistful of ice or snow alongside their meal will satisfy a frost giant, shadow giants hunger for the coagulated shadows of the Netherworld.

```statblock
creature: "Frost Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
