---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Redcap"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Low-Light Vision]]"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +15, Deception +11, Intimidation +13, Nature +10, Stealth +13"
abilityMods: ["+4", "+4", "+2", "+1", "+1", "+2"]
abilities_top:
  - name: "Red Cap"
    desc: "A redcap's woolen hat is dyed with the blood of their victims. If the redcap loses their cap, they no longer benefit from fast healing and take a –4 status penalty to their damage rolls. They can create a new cap in 10 minutes, but that cap doesn't grant them powers until the redcap has turned it red with Blood Soak. A cap has no benefit for creatures other than the redcap who made it. <br>  <br> > [!danger] Effect: Lost Red Cap"
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +15, **Will** +10"
health:
  - name: HP
    desc: "60; fast healing 10; **Weaknesses** cold iron 5"
abilities_mid:
  - name: "Fast Healing 10"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Divine Revulsion"
    desc: "If a redcap sees a creature brandish a religious symbol of a deity (which requires an Interact action by that creature) or cast a divine spell while wearing a religious symbol, the redcap must attempt a DC 19 [[Will]] save. They then become temporarily immune to all brandished religious symbols for 10 minutes. <br> - **Critical Success** The redcap is unaffected. <br> - **Success** The redcap is [[Frightened]] 2. <br> - **Failure** The redcap gains the [[Fleeing]] condition for 1 round and is [[Frightened]] 4."
  - name: "Deadly Cleave"
    desc: "`pf2:r` **Trigger** The redcap reduces a creature to 0 Hit Points with a halberd Strike <br>  <br> **Effect** The redcap makes another halberd Strike against a different creature, using the same multiple attack penalty as the halberd Strike that triggered this reaction. This counts toward their multiple attack penalty as normal."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Iron Boot +13 (`pf2:1`) (agile, versatile b), **Damage** 1d6+8 piercing"
  - name: "Melee strike"
    desc: "Halberd +15 (`pf2:1`) (reach 10 ft., versatile s), **Damage** 1d10+10 piercing"
spellcasting: []
abilities_bot:
  - name: "Blood Soak"
    desc: "`pf2:1` The redcap dips their cap in the blood of a slain foe. The foe must have died in the last minute, and the redcap must have helped kill it. The redcap gains a +4 status bonus to damage rolls for 1 minute. <br>  <br> > [!danger] Effect: Blood Soak"
  - name: "Stomp"
    desc: "`pf2:1` The redcap Strides up to half its Speed and makes a boot Strike at any point during that movement. If the boot Strike hits a [[Prone]] creature, it deals an extra 2d6 bleed."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Redcaps are sadistic and capricious fey who thrill in bloodletting and murder. While they are most famous for appearing as wizened, bearded men, redcaps of other genders are no less fearsome or cruel. However, redcaps are ultimately craven bullies, cowed by anything more powerful than themselves, a trait that leads them to fear and despise the symbols of deities.

Many fairy tales explain how the redcaps draw power from dipping the hats for which they are named in fresh blood. Just as iconic to these cruel little fey are their iron-clad boots, and the clanging sound of their metal soles clanking on stone floors is both discordant and disconcerting—especially to those who recognize the sound for what it is. Redcaps typically stand only 3 feet tall, with hunched frames, pointed ears, crooked teeth, and long, white, tangled hair.

Though unlikely to share true affection, redcaps find camaraderie in murder. Small troupes of redcaps travel together, sharing bloody kills and reminiscing on their brutal exploits. They loathe the company of most other creatures, with the notable exception of the feline fey called elananxes.

```statblock
creature: "Redcap"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
