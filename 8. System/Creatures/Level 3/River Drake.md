---
type: creature
group: ["Amphibious", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "River Drake"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: "Water"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Draconic"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +10, Intimidation +6, Stealth +9, Survival +7"
abilityMods: ["+3", "+4", "+2", "-1", "+2", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +11, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "45; **Immunities** paralyzed, sleep; **Resistances** acid 10"
abilities_mid:
  - name: "Tail Lash"
    desc: "`pf2:r` **Trigger** A creature within reach of the river drake's tail uses an action to Strike or attempt a skill check. <br>  <br> **Effect** The river drake attempts to Strike the triggering creature with its tail. If it hits, the creature takes a -2 circumstance penalty to the triggering roll. <br>  <br> > [!danger] Effect: Tail Lash"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +12 (`pf2:1`), **Damage** 2d8+3 piercing"
  - name: "Melee strike"
    desc: "Tail +12 (`pf2:1`) (reach 10 ft.), **Damage** 2d6+3 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Caustic Mucus"
    desc: "`pf2:2` The river drake spits a ball of caustic mucus up to a range of 50 feet that explodes in a @Template[burst|distance:10]. Creatures within the burst take @Damage[4d6[acid]|options:area-damage] damage (DC 19 [[Reflex]] save). Those that fail this save also take 1d6 persistent,acid damage and take a –5-foot status penalty to their Speed. This Speed reduction ends with the persistent acid damage. <br>  <br> The river drake can't use Caustic Mucus again for 1d6 rounds. <br>  <br> > [!danger] Effect: Caustic Mucus"
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The river drake makes one Fangs Strike and two Tail Strikes in any order."
  - name: "Speed Surge"
    desc: "`pf2:1` **Frequency** three times per day; <br>  <br> **Effect** The river drake Strides or Flies twice."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Although the glistening scales and sleek, fin-like wings on these drakes give them an appearance reminiscent of river fish, they are actually distant relatives of the dragons that rule the oceans. While smaller than most drakes, river drakes are more than capable of plaguing river travelers and are equally at home above and below the water's surface. This flexibility allows them to catch a wide variety of prey, from fish and boggards to deer and the occasional ferry passenger.

Ravenous, bestial, and driven by instinct, drakes are draconic monsters who bear a fraction of the terrifying might of the primal dragons they share evolutionary roots with. While they're weaker, slower, and less inclined toward reason than dragons, drakes are nonetheless a menace to creatures and settlements around them. Their propensity for forming raiding parties—small social groups fittingly called "rampages"—makes them all the more dangerous; a single rampage of river drakes can quickly lay waste to a waterside village, and roving rampages of desert drakes are a plague to caravan traders.

Drakes share a number of physical characteristics that unite them as one species despite their wide variety of habitats and abilities. For example, drakes lack forearms, leaving them with their formidable jaws and thickscaled tails to use in close combat. Most drakes would rather avoid this, however, preferring to use their magical breath to wreak havoc in wide swaths from comfortable distances while flying overhead. Finally, all drakes have small reservoirs of their ancestral draconic power that they can tap into to perform incredible feats of speed.

Different species of drakes rarely come into conflict. Part of this is their distinct habitats, but drakes are open to negotiating simple agreements between rampages. This courtesy does not extend to dragonets, which drakes happily take as prey. Solitary tamed drakes are also excluded from such agreements and considered free game if their tamer isn't strong enough to protect them.

Drake Eggs
While drake hides aren't any more valuable than those of similarly sized creatures, drake eggs are prized commodities. They are used as components in powerful spells as well as eaten by various cultures, but the most common use for drake eggs is hatching and rearing drakes to serve as mounts and guardians.

A typical drake lays a clutch of 2d4 eggs every 5 years. Eggs hatch within 3 to 6 weeks, during which time they must be kept in conditions appropriate to their natural environment, perhaps the most difficult aspect of drake husbandry. While it is generally easy for breeders to incubate the eggs of desert or jungle drakes (which require mildly warm temperatures to hatch) or river drakes (which must be submerged in running water), the eggs of flame and frost drakes require extreme temperatures in order to hatch, which can be difficult to replicate safely.

A drake egg is an object with Hardness 3, 5 HP, and no Broken Threshold. The coloration of drake eggs varies only slightly from one species to the next. A creature must succeed at a DC 20 [[Nature]] check, or a relevant DC 20 Lore check, to identify the drake species of a specific egg.

Once a drake hatches, they imprint on the first creature that they see. A creature imprinted on in this way can use Nature to Train and Command that drake. The market price of a drake egg varies depending on the type of drake and the exact legal situation. Because drakes are dangerous and intelligent creatures, many societies do not condone the trade of drake eggs and criminalize those who engage in it.

It takes 2 years for a drake hatchling to grow to full size. A well-trained drake can make a fearsome mount or guardian, but many careless would-be drake trainers are devoured by their charges.

```statblock
creature: "River Drake"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
