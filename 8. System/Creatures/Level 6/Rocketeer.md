---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rocketeer"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +13, Crafting +14, Performance +12, Engineering Lore +14"
abilityMods: ["+2", "+4", "+2", "+2", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +16, **Will** +14"
health:
  - name: HP
    desc: "85"
abilities_mid:
  - name: "Fuel Tank Vulnerability"
    desc: "When the rocketeer is struck by a critical hit that deals piercing or fire damage, they must attempt a DC 5 flat check. On a failure, the rocketeer's fuel tank explodes, dealing @Damage[6d6[fire]|options:area-damage] damage to the rocketeer and all creatures in a @Template[type:emanation|distance:20] and knocking the rocketeer [[Prone]]. The rocketeer loses their fly Speed and can't use Explosive Liftoff, Mid-air Collision, or Rocketing Strafe until they repair their jet pack, which requires an appropriate set of artisan's tools and takes 2 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Heavy Wrench +14 (`pf2:1`) (shove), **Damage** 1d6+8 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
  - name: "Ranged strike"
    desc: "Slide Pistol +17 (`pf2:1`) (capacity 5, concussive, fatal d10, reload 1, range 30 ft.), **Damage** 1d6+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Explosive Liftoff"
    desc: "`pf2:2` **Frequency** once per 10 minutes <br>  <br> **Requirements** The rocketeer is standing on a horizontal surface <br>  <br> **Effect** The rocketeer unleashes the full strength of their jets to launch themself into the air, dealing @Damage[7d6[fire],7d6[bludgeoning]|options:area-damage] damage to all creatures in a @Template[type:emanation|distance:15] with a DC 24 [[Reflex]] save. The rocketeer Flies twice, straight up into the air."
  - name: "Mid-air Collision"
    desc: "`pf2:2` The rocketeer Flies twice, then attempts to `act trip options=mid-air-collision` or `act shove options=mid-air-collision` another flying creature. If they roll a success on the Athletics check, they get a critical success instead."
  - name: "Rocketing Strafe"
    desc: "`pf2:2` The rocketeer Flies and makes two melee Strikes at any point during that movement. Each Strike must target a different creature. The rocketeer can forgo the melee Strikes to instead make one slide pistol Strike at any point during that movement and Interact to select the next loaded chamber of their slide pistol; they can do these in either order. Any Strike made as part of a Rocketing Strafe deals an additional 2d6 damage and takes the normal multiple attack penalty."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

It takes a very specific personality to strap on a tank filled with a highly flammable alchemical substance and set it afire to launch oneself into the sky, so it is perhaps unsurprising that most rocketeers are reckless and bombastic individuals who delight in the theatrics inherent in their craft. While the unpredictability of rocketeering devices and the high casualty rate among those who use them make such devices generally unsuitable for military applications, a few courageous souls have used them to become dashing folk heroes or performing daredevils, many of whose most memorable performances culminate in their own dramatic demises.

Although relatively uncommon across much of Golarion, the frequently eccentric but undeniably brilliant minds who create elaborate devices of clockwork, gunpowder, and steam often loom much larger in the public eye than their numbers would suggest.

```statblock
creature: "Rocketeer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
